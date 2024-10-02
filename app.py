from flask import Flask, jsonify

app = Flask(__name__)

# Sample crop data
crop_data = [

  {
    "crop_name": "Wheat",
    "variety": "Rajasthan Local",
    "state": "Rajasthan",
    "mandi_market": "Jaipur Mandi",
    "min_price": 2000,
    "max_price": 2500,
    "avg_price": 2250,
    "arrival_date": "2024-09-25"
  },
  {
    "crop_name": "Rice",
    "variety": "Basmati",
    "state": "Punjab",
    "mandi_market": "Ludhiana Mandi",
    "min_price": 3500,
    "max_price": 4000,
    "avg_price": 3750,
    "arrival_date": "2024-09-20"
  },
  {
    "crop_name": "Onion",
    "variety": "Red Onion",
    "state": "Maharashtra",
    "mandi_market": "Lasalgaon Mandi",
    "min_price": 1200,
    "max_price": 1500,
    "avg_price": 1350,
    "arrival_date": "2024-09-21"
  },
  {
    "crop_name": "Potato",
    "variety": "Kufri Jyoti",
    "state": "Uttar Pradesh",
    "mandi_market": "Agra Mandi",
    "min_price": 800,
    "max_price": 1000,
    "avg_price": 900,
    "arrival_date": "2024-09-22"
  },
  {
    "crop_name": "Tomato",
    "variety": "Hybrid",
    "state": "Karnataka",
    "mandi_market": "Bangalore Mandi",
    "min_price": 500,
    "max_price": 700,
    "avg_price": 600,
    "arrival_date": "2024-09-23"
  },
  {
    "crop_name": "Soybean",
    "variety": "Yellow",
    "state": "Madhya Pradesh",
    "mandi_market": "Indore Mandi",
    "min_price": 3500,
    "max_price": 4200,
    "avg_price": 3850,
    "arrival_date": "2024-09-26"
  },
  {
    "crop_name": "Cotton",
    "variety": "BT Cotton",
    "state": "Gujarat",
    "mandi_market": "Rajkot Mandi",
    "min_price": 5000,
    "max_price": 5500,
    "avg_price": 5250,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Sugarcane",
    "variety": "Co 86032",
    "state": "Tamil Nadu",
    "mandi_market": "Coimbatore Mandi",
    "min_price": 3000,
    "max_price": 3400,
    "avg_price": 3200,
    "arrival_date": "2024-09-22"
  },
  {
    "crop_name": "Maize",
    "variety": "Hybrid",
    "state": "Bihar",
    "mandi_market": "Patna Mandi",
    "min_price": 1400,
    "max_price": 1600,
    "avg_price": 1500,
    "arrival_date": "2024-09-23"
  },
  {
    "crop_name": "Groundnut",
    "variety": "Bold",
    "state": "Andhra Pradesh",
    "mandi_market": "Guntur Mandi",
    "min_price": 4500,
    "max_price": 5000,
    "avg_price": 4750,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Wheat",
    "variety": "MP Sharbati",
    "state": "Madhya Pradesh",
    "mandi_market": "Bhopal Mandi",
    "min_price": 2100,
    "max_price": 2600,
    "avg_price": 2350,
    "arrival_date": "2024-09-20"
  },
  {
    "crop_name": "Paddy",
    "variety": "IR 64",
    "state": "Chhattisgarh",
    "mandi_market": "Raipur Mandi",
    "min_price": 1800,
    "max_price": 2300,
    "avg_price": 2050,
    "arrival_date": "2024-09-22"
  },
  {
    "crop_name": "Chili",
    "variety": "Guntur Sannam",
    "state": "Andhra Pradesh",
    "mandi_market": "Guntur Mandi",
    "min_price": 9000,
    "max_price": 11000,
    "avg_price": 10000,
    "arrival_date": "2024-09-25"
  },
  {
    "crop_name": "Mustard",
    "variety": "Yellow",
    "state": "Haryana",
    "mandi_market": "Hissar Mandi",
    "min_price": 4200,
    "max_price": 4800,
    "avg_price": 4500,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Peas",
    "variety": "Green Peas",
    "state": "Himachal Pradesh",
    "mandi_market": "Shimla Mandi",
    "min_price": 3000,
    "max_price": 3500,
    "avg_price": 3250,
    "arrival_date": "2024-09-25"
  },
  {
    "crop_name": "Barley",
    "variety": "Rajasthan Local",
    "state": "Rajasthan",
    "mandi_market": "Kota Mandi",
    "min_price": 1500,
    "max_price": 1800,
    "avg_price": 1650,
    "arrival_date": "2024-09-23"
  },
  {
    "crop_name": "Pomegranate",
    "variety": "Bhagwa",
    "state": "Maharashtra",
    "mandi_market": "Pune Mandi",
    "min_price": 6000,
    "max_price": 7500,
    "avg_price": 6750,
    "arrival_date": "2024-09-22"
  },
  {
    "crop_name": "Banana",
    "variety": "Robusta",
    "state": "Tamil Nadu",
    "mandi_market": "Trichy Mandi",
    "min_price": 1200,
    "max_price": 1400,
    "avg_price": 1300,
    "arrival_date": "2024-09-21"
  },
  {
    "crop_name": "Cabbage",
    "variety": "Green Cabbage",
    "state": "West Bengal",
    "mandi_market": "Siliguri Mandi",
    "min_price": 800,
    "max_price": 1000,
    "avg_price": 900,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Cauliflower",
    "variety": "White",
    "state": "Uttar Pradesh",
    "mandi_market": "Lucknow Mandi",
    "min_price": 1000,
    "max_price": 1200,
    "avg_price": 1100,
    "arrival_date": "2024-09-20"
  },
  {
    "crop_name": "Carrot",
    "variety": "Red Carrot",
    "state": "Punjab",
    "mandi_market": "Amritsar Mandi",
    "min_price": 800,
    "max_price": 1000,
    "avg_price": 900,
    "arrival_date": "2024-09-26"
  },
  {
    "crop_name": "Brinjal",
    "variety": "Long Brinjal",
    "state": "Maharashtra",
    "mandi_market": "Nashik Mandi",
    "min_price": 600,
    "max_price": 800,
    "avg_price": 700,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Okra",
    "variety": "Hybrid",
    "state": "Karnataka",
    "mandi_market": "Mysore Mandi",
    "min_price": 1000,
    "max_price": 1200,
    "avg_price": 1100,
    "arrival_date": "2024-09-25"
  },
  {
    "crop_name": "Garlic",
    "variety": "Desi",
    "state": "Madhya Pradesh",
    "mandi_market": "Neemuch Mandi",
    "min_price": 2500,
    "max_price": 3000,
    "avg_price": 2750,
    "arrival_date": "2024-09-23"
  },
  {
    "crop_name": "Ginger",
    "variety": "Fresh",
    "state": "Kerala",
    "mandi_market": "Kochi Mandi",
    "min_price": 1500,
    "max_price": 1800,
    "avg_price": 1650,
    "arrival_date": "2024-09-21"
  },
  {
    "crop_name": "Turmeric",
    "variety": "Rajapuri",
    "state": "Tamil Nadu",
    "mandi_market": "Erode Mandi",
    "min_price": 6000,
    "max_price": 7000,
    "avg_price": 6500,
    "arrival_date": "2024-09-24"
  },
  {
    "crop_name": "Coriander",
    "variety": "Eagle",
    "state": "Rajasthan",
    "mandi_market": "Kota Mandi",
    "min_price": 5500,
    "max_price": 6000,
    "avg_price": 5750,
    "arrival_date": "2024-09-26"
  },
  {
    "crop_name": "Chana",
    "variety": "Desi",
    "state": "Madhya Pradesh",
    "mandi_market": "Harda Mandi",
    "min_price": 4200,
    "max_price": 4500,
    "avg_price": 4350,
    "arrival_date": "2024-09-25"
  },
  {
    "crop_name": "Moong Dal",
    "variety": "Green Moong",
    "state": "Rajasthan",
    "mandi_market": "Jaipur Mandi",
    "min_price": 6000,
    "max_price": 6800,
    "avg_price": 6400,
    "arrival_date": "2024-09-26"
  },
  {
    "crop_name": "Masoor Dal",
    "variety": "Red Masoor",
    "state": "Uttar Pradesh",
    "mandi_market": "Kanpur Mandi",
    "min_price": 5000,
    "max_price": 5500,
    "avg_price": 5250,
    "arrival_date": "2024-09-22"
  }
    # Add more crop entries here...
]

@app.route('/')
def home():
    return "Welcome to the Crop API!"

@app.route('/api/crops', methods=['GET'])
def get_crops():
    return jsonify(crop_data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
