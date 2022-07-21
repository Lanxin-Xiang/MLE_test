# MLE_test
Fetch Rewards Coding Assessment - Machine Learning Engineer

## Files
* calculator.py
* main.py
* Dockerfile
* requirements.txt

## How to run
### Use python
1. Run main.py
2. Run the following code in pyhton.

```
import requests, json

url="http://localhost:9000/api"
{data = json.dumps({"dimension":(3, 3), "corner points":  [(1, 1), (3, 1), (1, 3), (3, 3)]})}
r = requests.post(url, data)
print(r.json())
```

### In Docker
1. Build the image 
```
docker image build -t mle_test .
```
2. Run the container
```
docker run mle_test
```
3. Test with curl
```
curl -X POST http://localhost:9000/api -d "{\"dimension\": [3,3],\"corner points\":[[1, 1], [3, 1], [1, 3],[3, 3]]}"
```
