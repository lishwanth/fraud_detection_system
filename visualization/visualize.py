import redash_toolbelt

class DataVisualizer:
    def __init__(self, redash_api_key, redash_url):
        self.client = redash_toolbelt.Redash(redash_url, redash_api_key)

    def visualize(self, query_id):
        query = self.client.get_query_results(query_id)
        print(query)  # Here you can add code to process and visualize the data

if __name__ == "__main__":
    redash_api_key = 'your_redash_api_key'
    redash_url = 'http://localhost:5000'

    visualizer = DataVisualizer(redash_api_key, redash_url)
    visualizer.visualize(query_id=1)
