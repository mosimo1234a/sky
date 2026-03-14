from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# 모든 도메인에서 이 서버에 접근할 수 있도록 허용 (CORS 해결)
CORS(app)

OPENSKY_URL = "https://opensky-network.org/api/states/all"

@app.route('/api/flights')
def get_flights():
    # 아시아-태평양 지역 경계 설정 (대원님 코드의 범위와 동일)
    params = {
        'lamin': 20, 'lomin': 100, 'lamax': 60, 'lomax': 160
    }
    try:
        response = requests.get(OPENSKY_URL, params=params, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # 5000번 포트에서 서버 실행
    app.run(debug=True, port=5000)