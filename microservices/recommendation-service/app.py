from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database of all available services to run recommendations against
SERVICES_DATABASE = [
    {"id": 1, "name": "Electrician", "category": "Home Services", "price": 50, "description": "Wiring repair and fixture installation"},
    {"id": 2, "name": "Plumber", "category": "Home Services", "price": 60, "description": "Leak fixes and pipe installation"},
    {"id": 3, "name": "AC Repair", "category": "Home Services", "price": 80, "description": "AC maintenance and filter replacement"},
    {"id": 4, "name": "Internet Installation", "category": "Utility Services", "price": 40, "description": "Setup high-speed router and cabling"},
    {"id": 5, "name": "Water Supply Services", "category": "Utility Services", "price": 30, "description": "Water filtration and pipeline maintenance"},
    {"id": 6, "name": "Car Wash", "category": "Personal Services", "price": 25, "description": "Exterior and interior detail wash"},
    {"id": 7, "name": "Gardening", "category": "Personal Services", "price": 35, "description": "Lawn mowing and landscape design"},
    {"id": 8, "name": "Emergency Electrician", "category": "Emergency Services", "price": 100, "description": "24/7 urgent electrical support"},
    {"id": 9, "name": "Roadside Assistance", "category": "Emergency Services", "price": 90, "description": "Towing and tire replacement help"}
]

@app.route('/api/recommend', methods=['POST'])
def recommend_services():
    try:
        data = request.get_json() or {}
        preferred_category = data.get("preferredCategory", "").lower()
        search_query = data.get("searchQuery", "").lower()
        
        recommendations = []
        
        # Simulated AI Recommendation Algorithm: Scoring matching items
        for service in SERVICES_DATABASE:
            score = 0.0
            reasons = []
            
            # Match preferred category
            if preferred_category and service["category"].lower() == preferred_category:
                score += 0.6
                reasons.append(f"Matches your preferred category: {service['category']}")
                
            # Match search query words in name or description
            if search_query:
                query_words = search_query.split()
                matched_words = 0
                for word in query_words:
                    if word in service["name"].lower() or word in service["description"].lower():
                        matched_words += 1
                if matched_words > 0:
                    score += 0.35 * matched_words
                    reasons.append(f"Matches search query keywords")
                    
            # Fallback popularity/random weight to ensure variety
            if score == 0.0:
                # Add a baseline score for popular fallbacks (e.g. emergency services have higher baseline)
                if service["category"] == "Emergency Services":
                    score += 0.1
                    reasons.append("Highly requested emergency service")
                else:
                    score += 0.05
                    reasons.append("Frequently booked service near you")
            
            # Round score for readability
            score = round(score, 2)
            
            recommendations.append({
                "id": service["id"],
                "name": service["name"],
                "category": service["category"],
                "price": service["price"],
                "description": service["description"],
                "score": score,
                "reason": ", ".join(reasons) if reasons else "Recommended based on popularity"
            })
            
        # Sort recommendations by highest score first
        recommendations.sort(key=lambda x: x["score"], reverse=True)
        
        # Limit to top 3 recommendations
        top_recommendations = recommendations[:3]
        
        return jsonify({
            "status": "success",
            "recommendations": top_recommendations
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to generate recommendations",
            "details": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)
