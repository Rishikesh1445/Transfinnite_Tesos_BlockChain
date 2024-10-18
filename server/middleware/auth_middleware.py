from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from utils.auth_utils import decode_jwt_token
from typing import Dict

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> Dict:
    """
    Verify JWT token from Authorization header
    Returns decoded token payload if valid
    """
    print(credentials)
    if not credentials:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    print(token)
    token = credentials.credentials
    return decode_jwt_token(token)

def verify_admin(token_data: Dict) -> bool:
    """
    Example of role-based verification
    Can be expanded based on your needs
    """
    # Add your admin verification logic here
    # For example, check if user has admin role in token
    return token_data.get("role") == "admin"

def verify_user_access(token_data: Dict, user_id: str) -> bool:
    """
    Example of resource access verification
    Can be expanded based on your needs
    """
    return token_data.get("user_id") == user_id