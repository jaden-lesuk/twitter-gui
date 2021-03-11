import tweepy
import pandas as pd


def collect_entities(entities, entity, entity_attribute):
    collect_list = []
    if entity in entities:
        for item in entities[entity]:
            collect_list.append(item[entity_attribute])
    return collect_list


def ratio(num_one, num_two):
    if num_two == 0:
        return 1
    elif num_one == 0:
        return 0
    else:
        answer = round(num_one / num_two, 2)
        return answer


def collect(method, api_key, api_key_secret, access_token, access_token_secret, query, max_number, file_location):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print('Authentication Successful')
    except Exception:
        return "Authentication Failed"

    if method == 0:
        all_attributes = ['id', 'text', 'source', 'lang', 'created_at', 'favourite_count', 'retweet_count',
                          'in_reply_to_status_id', 'in_reply_to_screen_name', 'in_reply_to_user_id', 'favorited',
                          'retweeted', 'possibly_sensitive', 'truncated', 'query', 'url', 'user_id', 'user_name',
                          'user_screen_name', 'user_description', 'user_created_at', 'user_tweets_count',
                          'user_favorites_count', 'user_followers_count', 'user_friends_count', 'user.listed_count',
                          'user_location', 'user_lang', 'user_utc_offset', 'user_url', 'user_profile_image_url',
                          'user_profile_image_url_https', 'user_default_profile_image', 'following_to_followers_ratio',
                          'tweets_to_following_ratio', 'favorties_to_following_ratio', 'tweets_to_favorites_ratio',
                          'entities_user_mentions', 'entities_hashtags', 'entities_urls', 'entities_media',
                          'is_retweet',
                          'original_tweet_id', 'original_tweet_text', 'original_tweet_source', 'original_tweet_lang',
                          'original_tweet_created_at', 'original_user_id', 'original_user_name',
                          'original_user_screen_name', 'original_user_tweet_count', 'original_user_favorites_count',
                          'original_user_followers_count', 'original_user_following_count',
                          'original_user_listed_count']

        all_tweets = []
        print('Collecting Tweets')

        max_number = int(max_number)
        count = 0

        try:
            for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended').items(max_number):

                count += 1
                print(count)

                frame = []

                # Tweet Details
                frame.append(tweet.id)
                frame.append(tweet.full_text)
                frame.append(tweet.source)

                frame.append(getattr(tweet, 'lang', ""))

                frame.append(tweet.created_at)
                frame.append(getattr(tweet, 'favourite_count', ""))
                frame.append(tweet.retweet_count)

                frame.append(getattr(tweet, 'in_reply_to_status_id', ""))
                frame.append(getattr(tweet, 'in_reply_to_screen_name', ""))
                frame.append(getattr(tweet, 'in_reply_to_user_id', ""))
                frame.append(getattr(tweet, 'favorited', ""))

                frame.append(tweet.retweeted)
                frame.append(getattr(tweet, 'possibly_sensitive', ""))
                frame.append(tweet.truncated)
                frame.append(query)
                frame.append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")

                # User Details
                frame.append(tweet.user.id)
                frame.append(tweet.user.name)
                frame.append(tweet.user.screen_name)
                frame.append(getattr(getattr(tweet, 'user', None), "description", ""))

                frame.append(tweet.user.created_at)
                frame.append(tweet.user.statuses_count)
                frame.append(tweet.user.favourites_count)
                frame.append(tweet.user.followers_count)
                frame.append(tweet.user.friends_count)
                frame.append(tweet.user.listed_count)
                frame.append(getattr(getattr(tweet, 'user', None), "location", ""))
                frame.append(tweet.user.lang)
                frame.append(tweet.user.utc_offset)
                frame.append(getattr(getattr(tweet, 'user', None), "url", ""))
                frame.append(tweet.user.profile_image_url)
                frame.append(tweet.user.profile_image_url_https)
                frame.append(tweet.user.default_profile_image)

                # User Metrics Ratios
                frame.append(ratio(tweet.user.friends_count, tweet.user.followers_count))
                frame.append(ratio(tweet.user.statuses_count, tweet.user.friends_count))
                frame.append(ratio(tweet.user.favourites_count, tweet.user.friends_count))
                frame.append(ratio(tweet.user.statuses_count, tweet.user.favourites_count))

                # tweet entities
                frame.append(collect_entities(tweet.entities, 'user_mentions', 'screen_name'))
                frame.append(collect_entities(tweet.entities, 'hashtags', 'text'))
                frame.append(collect_entities(tweet.entities, 'urls', 'expanded_url'))
                frame.append(collect_entities(tweet.entities, 'media', 'media_url'))

                if hasattr(tweet, 'retweeted_status'):
                    tweet_is_retweet = True
                    frame.append(tweet_is_retweet)

                    # Retweeted Tweet
                    frame.append(tweet.retweeted_status.id)
                    frame.append(tweet.retweeted_status.full_text)
                    frame.append(tweet.retweeted_status.source)
                    frame.append(getattr(getattr(tweet, 'retweeted_status', None), "lang", ""))
                    frame.append(tweet.retweeted_status.created_at)

                    # Retweeted User
                    frame.append(tweet.retweeted_status.user.id)
                    frame.append(tweet.retweeted_status.user.name)
                    frame.append(tweet.retweeted_status.user.screen_name)
                    frame.append(tweet.retweeted_status.user.statuses_count)
                    frame.append(tweet.retweeted_status.user.favourites_count)
                    frame.append(tweet.retweeted_status.user.followers_count)
                    frame.append(tweet.retweeted_status.user.friends_count)
                    frame.append(tweet.retweeted_status.user.listed_count)

                else:
                    tweet_is_retweet = False
                    frame.append(tweet_is_retweet)
                    frame.extend(["", "", "", "", "", "", "", "", "", "", "", "", ""])

                frame = [frame]
                all_tweets.extend(frame)
            print('Collection Successful')
            print('Converting to csv...')
            tweets = pd.DataFrame(all_tweets, columns=all_attributes)
            path = f'{file_location}/{query}_tweets.csv'
            tweets.to_csv(path, index=False)
            return f"Successful! stored at {query}_tweets.csv"
        except FileNotFoundError:
            return "File Location Incorrect"
        except Exception as e:
            return "Error"

    elif method == 2:
        try:
            print('Collecting Following')
            all_following = []
            count = 0

            pages = tweepy.Cursor(api.friends, screen_name=query, count=200).pages()

            for page in pages:
                for user in page:
                    count += 1
                    print(count)

                    frame = []
                    user_screen_name = user.screen_name
                    user_follower_count = user.followers_count
                    user_following_count = user.friends_count
                    frame.append([user_screen_name, user_follower_count, user_following_count])
                    all_following.extend(frame)

            following = pd.DataFrame(all_following, columns=['Screen Name', 'Follower Count', 'Following Count'])
            print('Collection Successful')
            print('Converting to csv...')
            path = f'{file_location}/{query}_following.csv'
            following.to_csv(path, index=False)
            return f"Successful! stored at {query}_following.csv"
        except FileNotFoundError:
            return "File Location Incorrect"
        except Exception as e:
            return "Error"

    elif method == 1:
        try:
            print('Collecting Followers')
            all_followers = []
            count = 0

            pages = tweepy.Cursor(api.followers, screen_name=query, count=200).pages()

            for page in pages:
                for user in page:
                    count += 1
                    print(count)

                    frame = []
                    user_screen_name = user.screen_name
                    user_follower_count = user.followers_count
                    user_following_count = user.friends_count
                    frame.append([user_screen_name, user_follower_count, user_following_count])
                    all_followers.extend(frame)

            followers = pd.DataFrame(all_followers, columns=['Screen Name', 'Follower Count', 'Following Count'])
            print('Collection Successful')
            print('Converting to csv...')
            path = f'{file_location}/{query}_followers.csv'
            followers.to_csv(path, index=False)
            return f"Successful! stored at {query}_followers.csv"

        except FileNotFoundError:
            return "File Location Incorrect"
        except Exception as e:
            return "Error"