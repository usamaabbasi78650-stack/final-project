# Database Schema (MongoDB / Mongoose)

## 1. User Collection
```json
{
  "_id": "ObjectId",
  "name": "String",
  "email": "String (Unique)",
  "passwordHash": "String",
  "role": "Enum['Customer', 'Provider', 'Admin']",
  "createdAt": "Date"
}
```

## 2. Service Collection
```json
{
  "_id": "ObjectId",
  "name": "String",
  "category": "Enum['Home', 'Utility', 'Personal', 'Emergency']",
  "description": "String",
  "price": "Number",
  "providerId": "ObjectId (ref: User)",
  "status": "Enum['Active', 'Inactive']"
}
```

## 3. Booking Collection
```json
{
  "_id": "ObjectId",
  "customerId": "ObjectId (ref: User)",
  "serviceId": "ObjectId (ref: Service)",
  "providerId": "ObjectId (ref: User)",
  "status": "Enum['Pending', 'Confirmed', 'Completed', 'Cancelled']",
  "appointmentDate": "Date",
  "paymentStatus": "Enum['Unpaid', 'Paid']"
}
```
