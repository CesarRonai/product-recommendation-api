# 🚀 Product Recommendation API with FastAPI & AWS

This project implements a **Product Recommendation System** using **SVD (Singular Value Decomposition)**, trained with the **Surprise** library and deployed via **FastAPI**. The model is hosted on **AWS EC2**, providing a scalable and efficient recommendation API.

## 📖 Table of Contents
- Overview
- Technologies Used
- AWS Deployment
- Project Structure
- How to Run Locally
- API Endpoints
- Example Response
- Next Steps
- License
- Contact

## Overview
This project is an API that receives a **customer ID** and returns the **N most recommended products** based on their purchase history. We use the **SVD algorithm**, which learns latent patterns for personalized recommendations.

### Features
- **Personalized product recommendations** based on customer behavior.
- **Deployed on AWS EC2**, making the API accessible from anywhere.
- **Built with FastAPI**, ensuring fast and scalable responses.

## Technologies Used
- **Programming Language**: Python 3.9+
- **API Framework**: FastAPI
- **Machine Learning**: Surprise (SVD)
- **Data Processing**: Pandas
- **Deployment**: AWS EC2, Uvicorn

## AWS Deployment
1️⃣ **Creating an EC2 Instance**  
   - Ubuntu 22.04 LTS with `t2.micro` (Free Tier)  

2️⃣ **Installing Dependencies**  
   ```bash
   sudo apt update && sudo apt install python3-pip -y
   pip3 install fastapi uvicorn pandas scikit-surprise boto3
   ```

3️⃣ **Transferring the Project to EC2**  
   ```bash
   scp -i "your-key.pem" api_recommendation.py matriz_cliente_produto.csv modelo_svd.pkl ubuntu@your-ec2-ip:~
   ```

4️⃣ **Running the API**  
   ```bash
   uvicorn api_recommendation:app --host 0.0.0.0 --port 8000 --reload
   ```

5️⃣ **Accessing the API**  
   ```
   http://your-ec2-ip:8000/
   ```

## Project Structure
```
📂 recommendation-api/
│── 📂 models/                # Trained models
│── 📂 app/                   # API source code
│   │── __init__.py           # Indicates a Python module
│   │── api_recommendation.py # API implementation
│── 📜 requirements.txt       # Dependencies
│── 📜 README.md              # Project documentation
│── 📜 .gitignore             # Ignored files in GitHub
```

## How to Run Locally
1️⃣ **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR-USERNAME/recommendation-api.git
   cd recommendation-api
   ```

2️⃣ **Create a virtual environment and install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3️⃣ **Start the API**  
   ```bash
   uvicorn app.api_recommendation:app --reload
   ```

4️⃣ **Test the API**  
   ```
   http://127.0.0.1:8000/
   ```

5️⃣ **Get recommendations**  
   ```
   http://127.0.0.1:8000/predict?customer_unique_id=EXAMPLE123&n=5
   ```

## API Endpoints
1️⃣ **`/` - API Status**  
   - **Method:** `GET`  
   - **Description:** Returns a welcome message.  

   **Example Response**  
   ```json
   {
     "message": "Product Recommendation API - FastAPI"
   }
   ```

2️⃣ **`/predict` - Get Product Recommendations**  
   - **Method:** `GET`  
   - **Parameters:**  
     - `customer_unique_id` (string) → Customer ID  
     - `n` (int) → Number of recommendations (default = 5)  
   - **Description:** Returns the N most recommended products.  

   **Example Request**  
   ```
   http://your-ec2-ip:8000/predict?customer_unique_id=EXAMPLE123&n=5
   ```

   **Example Response**  
   ```json
   {
     "customer_unique_id": "EXAMPLE123",
     "recommendations": [
       ["product_A", 4.89],
       ["product_B", 4.75],
       ["product_C", 4.63]
     ]
   }
   ```

## Example Response
```json
{
  "customer_unique_id": "C12345",
  "recommendations": [
    ["f3720bc68555b1bff49bff41b017ac", 3.931],
    ["e7cc48a9daff5436f3d3aad9426f28b", 3.684],
    ["c04ca4b9c924494cf82e0fba966f955", 3.575]
  ]
}
```
## Instalação

Siga os passos abaixo para configurar o ambiente local:

1. **Clone repositório:**
   ```bash
   git clone https://github.com/CesarRonai/product-recommendation-api.git
   cd product-recommendation-api

## Next Steps
✅ **Deploy the API to AWS (EC2 or SageMaker)**  
✅ **Optimize API performance for real-time recommendations**  
✅ **Improve model explainability (better scoring insights)**  
⬜ **Automate model retraining with new customer data**  
⬜ **Monitor API usage and implement logging**  

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or suggestions, reach out via GitHub!  
📧 **Email:** cesar.ronai@hotmail.com  

## Deploying to GitHub
```bash
git add README.md
git commit -m "Added full project documentation"
git push origin main
```
```
