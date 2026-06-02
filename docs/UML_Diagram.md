# QuickServe UML Class Diagram

This UML diagram represents the core architecture of the QuickServe application, illustrating the relationships between Users, Services, Bookings, Payments, and Reviews.

```mermaid
classDiagram
    %% Ensuring clean relationships and structure
    
    class User {
        +ObjectId _id
        +String name
        +String email
        +String passwordHash
        +String phone
        +String address
        +Enum role
        +Date createdAt
        +register()
        +login()
        +updateProfile()
    }

    class Customer {
        +browseServices()
        +bookService()
        +leaveReview()
    }

    class Provider {
        +List~ObjectId~ offeredServices
        +Enum availabilityStatus
        +Float averageRating
        +acceptBooking()
        +updateServiceStatus()
    }

    class Admin {
        +manageUsers()
        +manageServices()
        +viewAnalytics()
    }

    class Service {
        +ObjectId _id
        +String name
        +Enum category
        +String description
        +Float price
        +ObjectId providerId
        +Enum status
        +createService()
        +updateService()
        +deleteService()
    }

    class Booking {
        +ObjectId _id
        +ObjectId customerId
        +ObjectId serviceId
        +ObjectId providerId
        +Date appointmentDate
        +Enum status
        +Enum paymentStatus
        +createBooking()
        +cancelBooking()
        +completeBooking()
    }

    class Payment {
        +ObjectId _id
        +ObjectId bookingId
        +Float amount
        +String transactionId
        +Date paymentDate
        +Enum status
        +processPayment()
        +refundPayment()
    }

    class Review {
        +ObjectId _id
        +ObjectId customerId
        +ObjectId serviceId
        +Integer rating
        +String comment
        +Date datePosted
        +addReview()
        +deleteReview()
    }

    %% Relationships with straight association arrows
    User <|-- Customer : "Inherits"
    User <|-- Provider : "Inherits"
    User <|-- Admin : "Inherits"
    
    Provider "1" --> "*" Service : "Offers"
    Customer "1" --> "*" Booking : "Makes"
    Provider "1" --> "*" Booking : "Receives"
    Service "1" --> "*" Booking : "Included in"
    
    Booking "1" --> "1" Payment : "Requires"
    Customer "1" --> "*" Review : "Writes"
    Service "1" --> "*" Review : "Has"
```
