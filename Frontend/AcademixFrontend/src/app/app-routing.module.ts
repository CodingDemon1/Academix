import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './AllComponents/dashboard/dashboard.component';
import { HomeComponent } from './AllComponents/home/home.component';
import { InstructorLoginComponent } from './AllComponents/instructor-login/instructor-login.component';
import { StudentLoginComponent } from './AllComponents/student-login/student-login.component';
import { InstructorCoursesComponent } from './AllComponents/instructor-courses/instructor-courses.component';
import { InstructorAssignmentsComponent } from './AllComponents/instructor-assignments/instructor-assignments.component';
import { StudentCoursesComponent } from './AllComponents/student-courses/student-courses.component';
import { StudentAssignmentsComponent } from './AllComponents/student-assignments/student-assignments.component';
import { InstructorDashboardComponent } from './AllComponents/instructor-dashboard/instructor-dashboard.component';
import { StudentDashboardComponent } from './AllComponents/student-dashboard/student-dashboard.component';
import { InstructorProfileComponent } from './AllComponents/instructor-profile/instructor-profile.component';
import { StudentProfileComponent } from './AllComponents/student-profile/student-profile.component';
import { SingleAssignmentComponent } from './AllComponents/single-assignment/single-assignment.component';
import { StudentEnrollmentsComponent } from './AllComponents/student-enrollments/student-enrollments.component';

const routes: Routes = [
  {
    path:"",component:HomeComponent
  },
  {
    path:"home", component: HomeComponent
  },
  {
    path:"instructorlogin", component:InstructorLoginComponent,
  },
  {
    path:"studentlogin", component: StudentLoginComponent
  },
  { path: 'instructor-dashboard', 
    component: InstructorDashboardComponent,
    children:[
      { path: '',pathMatch:'full', redirectTo: 'instructor' },
      { path: 'instructor', component: InstructorCoursesComponent },
      { path: 'instructor/assignments/:cId', component: InstructorAssignmentsComponent },
      { path: 'instructor/profile', component: InstructorProfileComponent },
      { path:'instructor/i-assignment/:aId/', component: SingleAssignmentComponent}
    ]
  },
  { path: 'student-dashboard', 
    component: StudentDashboardComponent,
    children:[
      
      { path: '', pathMatch:"full",redirectTo:'student' },
      { path: 'student', component: StudentCoursesComponent, pathMatch:"full" },
      { path: 'student/assignments', component: StudentAssignmentsComponent, pathMatch:"full"  },
      { path: 'student/profile', component: StudentProfileComponent, pathMatch:"full" },
      { path: 'student/enrollments', component: StudentEnrollmentsComponent, pathMatch:"full" },
    ]
  },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
