Small util files to make certain repetitive tasks easier:

async_json_url_node_checker.py

Simply add a list of urls (that return json else change the fetch function) to compare the returned results.
All results should be the same as determined by: key=lambda i, p: i == p

