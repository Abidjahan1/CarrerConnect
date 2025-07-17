# CareerConnect – Full Stack Job Portal

**CareerConnect** is a robust, end-to-end job portal built using **Django** and **PostgreSQL** with a secure login system, role-based access, application tracking, resume uploads, and admin-level task management. It supports both job seekers (applicants) and organization HR/admins, featuring an extendable workflow for handling shortlisting and hiring.



## 🛠 Tech Stack

- **Backend:** Django (Python), Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** HTML, Bootstrap
- **Authentication:** Django Auth (Built-in)
- **Admin Panel:** Django Admin (Customized Roles & Permissions)
- **File Handling:** Django FileField (CV/Resume Uploads)
- **Deployment Ready:** Configurable for Heroku, Railway, Hostinger, or VPS

---

## ✅ Features by Phase

### Phase 1: Basic Job Listing & Application
- Job posts viewable to all visitors
- User authentication system (Sign up/Login)
- Applicants can apply to jobs with resume upload

### Phase 2: Role-Based Access
- Admin/HR roles using Django groups
- Job listing, application, and user dashboards are role-restricted

### Phase 3: Application Dashboard
- Applicants can see all jobs they’ve applied to
- Application status tracking: Pending, Shortlisted, Rejected, Hired

### Phase 4: Resume Uploads & CV Viewer
- Secure CV/Resume uploads (PDF, DOC)
- View resume from admin/applicant dashboard

### Phase 5: Job Posting via Admin Panel
- Jobs added directly from Django Admin
- Auto timestamps and user tracking

### Phase 6: Job Expiry System
- Auto-hide expired jobs from applicant view
- Expiry status managed from job model/admin panel

### Phase 7: Hide Apply Button for Duplicate Application
- If already applied, apply button is disabled with "Already Applied" tag

### Phase 8: Admin-Level Application Control
- Super Admin can view all applications
- Admins can assign shortlisting tasks to specific HR team members

### Phase 9: Application Status Badges
- Beautiful colored badges for: `Pending`, `Shortlisted`, `Rejected`, `Hired`
- Bootstrap-based, responsive UI



---


