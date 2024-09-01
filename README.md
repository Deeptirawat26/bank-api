# Bank API Documentation

## Overview

This API provides access to information about banks and their branches. Below are the available endpoints and their functionalities.

## API Endpoints

### 1. List All Banks

**Endpoint**: `/banks/`  
**Method**: `GET`  
**Description**: Retrieves a list of all banks.  
**Response**: A JSON array of bank objects, each containing details about the banks.

### 2. Get Details of a Specific Bank

**Endpoint**: `/banks/<id>/`  
**Method**: `GET`  
**Description**: Retrieves details of a specific bank by its ID.  
**Parameters**:
- `<id>`: The unique identifier for the bank.  
**Response**: A JSON object containing details about the specified bank.

### 3. Get Details of a Specific Branch

**Endpoint**: `/branches/<ifsc>/`  
**Method**: `GET`  
**Description**: Retrieves all details of a specific branch by its IFSC code.  
**Parameters**:
- `<ifsc>`: The IFSC code of the branch.  
**Response**: A JSON object containing detailed information about the specified branch.

## Example Requests

### 1. List All Banks

```sh
curl -X GET http://localhost:8000/banks/
```

### 2. Get Details of a Specific Bank

```sh
curl -X GET http://localhost:8000/banks/1/
```

### 3. Get Details of a Specific Branch

```sh
curl -X GET http://localhost:8000/branches/ABHY0065001/
```

## Setup and Installation

1. **Clone the Repository**

   ```sh
   git clone [<repository-url>](https://github.com/Deeptirawat26/bank-api)
   ```

2. **Navigate to the Project Directory**

   ```sh
   cd bank-api
   ```


3. **Apply Migrations**

   ```sh
   python manage.py migrate
   ```

4. **Run the Development Server**

   ```sh
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`.

