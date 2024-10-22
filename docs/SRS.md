# Software Requirements Specification
## Introduction
1.1 Purpose
TaskMangerApp Version 0.1.1. It will allow a user to create, edit, delete, mark completed and filter diffferent tasks


1.2 Document Conventions
Describe any standards or typographical conventions that were followed when writing this SRS, such as fonts or highlighting that have special significance. For example, state whether priorities for higher-level requirements are assumed to be inherited by detailed requirements, or whether every requirement statement is to have its own priority.

1.3 Intended Audience and Reading Suggestions
Developers: responsible for coding and testing code.
Project mangers: Scrum master and Report manager responsible for creating tasks, giving out tasks, meeting reports. 
The rest of the SRS document is about the scope of the Task Manager App using the agile methodology. The overall description is for everyone to read. The other parts are for the Project managers and developers. You should start with reading the overall description and then you can move on to other part.   


1.4 Product Scope
The software being specified is the Task Manager App. The purpose of the app is to allow users to do different things with tasks that they have. Some of the benefits include allowing a person to organize their daily tasks improving productivity and organization.  


1.5 References
Use case document, other diagrams.


## Overall Description
2.1 Product Perspective:
Completely new stand alone application

2.2 Product Functions:
Allow users to create, edit, delete, and manage tasks.

2.3 User Classes and Characteristics:
Average customer. All customers will use the app the same.

2.4 Operating Environment:
CLI required.

2.5 Design and Implementation Constraints:
N/A. Simple application.

2.6 User Documentation:
Simple tutorial in the CLI.

2.7 Assumptions and Dependencies:
N/A

## External Interface Requirements
3.1 User Interfaces
Describe the logical characteristics of each interface between the software product and the users. This may include sample screen images, any GUI standards or product family style guides that are to be followed, screen layout constraints, standard buttons and functions (e.g., help) that will appear on every screen, keyboard shortcuts, error message display standards, and so on. Define the software components for which a user interface is needed. Details of the user interface design should be documented in a separate user interface specification.

3.2 Hardware Interfaces
Describe the logical and physical characteristics of each interface between the software product and the hardware components of the system. This may include the supported device types, the nature of the data and control interactions between the software and the hardware, and communication protocols to be used.

3.3 Software Interfaces
Describe the connections between this product and other specific software components (name and version), including databases, operating systems, tools, libraries, and integrated commercial components. Identify the data items or messages coming into the system and going out and describe the purpose of each. Describe the services needed and the nature of communications. Refer to documents that describe detailed application programming interface protocols. Identify data that will be shared across software components. If the data sharing mechanism must be implemented in a specific way (for example, use of a global data area in a multitasking operating system), specify this as an implementation constraint.

3.4 Communications Interfaces
Describe the requirements associated with any communications functions required by this product, including e-mail, web browser, network server communications protocols, electronic forms, and so on. Define any pertinent message formatting. Identify any communication standards that will be used, such as FTP or HTTP. Specify any communication security or encryption issues, data transfer rates, and synchronization mechanisms.

## 4. System Features

This section explains the key features of the Task Manager app, focusing on simple descriptions and functional requirements.

### 4.1 Task Creation and Management

#### 4.1.1 Description and Priority
Users can create, edit, delete, and manage tasks with priorities and deadlines.
- **Priority**: High

#### 4.1.2 Functional Requirements
- Users can add tasks with a title, description, due date, and priority.
- Tasks must have a valid title (not empty).
- Tasks should display in a list sorted by due date or priority.
- Users can edit or delete tasks, with confirmation before deletion.
- Notifications should be sent for upcoming or overdue tasks.

### 4.2 Task Status Tracking

#### 4.2.1 Description and Priority
Users can track task progress by marking them as "To Do," "In Progress," or "Completed."
- **Priority**: High

#### 4.2.2 Functional Requirements
- Users can update the status of tasks.
- Tasks should move to the appropriate section based on status (e.g., "Completed" section).
- Users can revert a "Completed" task back to "In Progress."

### 4.3 Task Sorting and Filtering

#### 4.3.1 Description and Priority
Users can sort and filter tasks by priority, due date, or other criteria.
- **Priority**: Medium

#### 4.3.2 Functional Requirements
- Users can sort tasks by due date or priority.
- Filters should show tasks based on criteria like status or deadline.
- The app saves user preferences for sorting/filtering.

### 4.4 Notifications and Reminders

#### 4.4.1 Description and Priority
Users receive reminders for tasks that are due soon or overdue.
- **Priority**: Medium

#### 4.4.2 Functional Requirements
- Notifications are sent 24 hours before a task is due.
- Overdue tasks are highlighted, and users are reminded.

## Other Nonfunctional Requirements
5.1 Performance Requirements
The app needs to repond to task creation and editing within a timely manner.

5.2 Safety Requirements
Specify those requirements that are concerned with possible loss, damage, or harm that could result from the use of the product. Define any safeguards or actions that must be taken, as well as actions that must be prevented. Refer to any external policies or regulations that state safety issues that affect the product’s design or use. Define any safety certifications that must be satisfied.

5.3 Security Requirements
Specify any requirements regarding security or privacy issues surrounding use of the product or protection of the data used or created by the product. Define any user identity authentication requirements. Refer to any external policies or regulations containing security issues that affect the product. Define any security or privacy certifications that must be satisfied.

5.4 Software Quality Attributes
This app needs to be adaptable to different types of tasks, easily maintainable, consistent in functionality, and fully testable.

5.5 Business Rules
This product should be usable and functional to any person in any role.

## Other Requirements
Define any other requirements not covered elsewhere in the SRS. This might include database requirements, internationalization requirements, legal requirements, reuse objectives for the project, and so on. Add any new sections that are pertinent to the project.

Appendix A: Glossary
Define all the terms necessary to properly interpret the SRS, including acronyms and abbreviations. You may wish to build a separate glossary that spans multiple projects or the entire organization, and just include terms specific to a single project in each SRS.

Appendix B: Analysis Models
Optionally, include any pertinent analysis models, such as data flow diagrams, class diagrams, state-transition diagrams, or entity-relationship diagrams.

Appendix C: To Be Determined List
Collect a numbered list of the TBD (to be determined) references that remain in the SRS so they can be tracked to closure.
