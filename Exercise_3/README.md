# Chuck Norris Jokes API

This API provides random Chuck Norris jokes. You can use it to get funny and entertaining jokes related to the famous actor and martial artist, Chuck Norris.

## Using the API

The Chuck Norris Jokes API can be used by making an HTTP GET request to the following URL:

```
https://api.chucknorris.io/jokes/random
```

The API response will be a JSON object that contains the Chuck Norris joke. Here's an example response:

```json
{
  "categories": [],
  "created_at": "2022-05-15 10:20:56.305544",
  "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
  "id": "cqo2S2FHTA6uU_1-oKgHtg",
  "updated_at": "2022-05-15 10:20:56.305544",
  "url": "https://api.chucknorris.io/jokes/cqo2S2FHTA6uU_1-oKgHtg",
  "value": "Chuck Norris doesn't sleep. He waits."
}
```

The Chuck Norris joke can be found in the `"value"` property of the JSON object.

## Example Code in Python

Here's an example of how to use the Chuck Norris Jokes API in Python using the `requests` library:

```python
import requests

# Make the API call
response = requests.get('https://api.chucknorris.io/jokes/random')

# Check the response status code
if response.status_code == 200:
    data = response.json()
    joke = data['value']
    print('Chuck Norris Joke:', joke)
else:
    print('Error making the request:', response.status_code)
```

This example makes an HTTP GET request to the API URL and prints the Chuck Norris joke in the console.

## Contributions

Contributions to the Chuck Norris Jokes API are welcome. If you have any ideas to improve the API, you can fork the repository and submit a pull request with your changes.

## Credits

This program was developed by Victoria Romero.

The Chuck Norris Jokes API is provided by the chucknorris.io website.

The base code and its explanation are based on the tutorial provided by MoureDev.