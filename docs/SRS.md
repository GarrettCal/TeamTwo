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

## System Features
This template illustrates organizing the functional requirements for the product by system features, the major services provided by the product. You may prefer to organize this section by use case, mode of operation, user class, object class, functional hierarchy, or combinations of these, whatever makes the most logical sense for your product.

4.1 System Feature 1
Don’t really say “System Feature 1.” State the feature name in just a few words. 4.1.1 Description and Priority Provide a short description of the feature and indicate whether it is of High, Medium, or Low priority. You could also include specific priority component ratings, such as benefit, penalty, cost, and risk (each rated on a relative scale from a low of 1 to a high of 9). 4.1.2 Stimulus/Response Sequences List the sequences of user actions and system responses that stimulate the behavior defined for this feature. These will correspond to the dialog elements associated with use cases. 4.1.3 Functional Requirements Itemize the detailed functional requirements associated with this feature. These are the software capabilities that must be present in order for the user to carry out the services provided by the feature, or to execute the use case. Include how the product should respond to anticipated error conditions or invalid inputs. Requirements should be concise, complete, unambiguous, verifiable, and necessary. Use “TBD” as a placeholder to indicate when necessary information is not yet available.

Each requirement should be uniquely identified with a sequence number or a meaningful tag of some kind.

4.2 System Feature 2 (and so on)
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
