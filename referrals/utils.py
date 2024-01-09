import uuid


# Function to generate the code max of 12 
def generate_ref_code():
    
    code = str(uuid.uuid4()).replace("-","")[:12]
    
    return code