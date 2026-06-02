# Final Report: QuickServe

## 1. Process Model: Agile/Scrum
We adopted Agile methodology for this project to allow for continuous feedback and incremental development. 
- **Sprint Planning:** We broke down features into 1-week sprints.
- **Why Agile:** It allowed us to adapt to requirement changes easily compared to the rigid Waterfall model.

## 2. Software Process Improvement (SPI)
Through iterative development, we significantly improved UI load times by lazy-loading components and optimized our database queries after analyzing the initial prototype's performance bottlenecks.

## 4. Lehman's Laws Justification
- **Continuing Change:** As the system was used, we had to add new service categories (Law of Continuing Change).
- **Increasing Complexity:** Refactoring was necessary in Sprint 4 to manage the growing complexity of the booking logic (Law of Increasing Complexity).

## 6. Refactoring
We refactored the monolith API into modular routes (`routes/users.js`, `routes/services.js`) to improve maintainability and remove duplicated validation logic.

## 11. Team Roles
- Frontend Developer: Built React components.
- Backend Developer: Configured Express and MongoDB.
- QA Tester: Wrote Jest unit tests.
