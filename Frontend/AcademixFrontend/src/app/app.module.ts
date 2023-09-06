import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './AllComponents/dashboard/dashboard.component';
import { NavbarComponent } from './AllComponents/navbar/navbar.component';
import { HomeComponent } from './AllComponents/home/home.component';
import { StudentLoginComponent } from './AllComponents/student-login/student-login.component';
import { InstructorLoginComponent } from './AllComponents/instructor-login/instructor-login.component';
import { InstructorDashboardComponent } from './AllComponents/instructor-dashboard/instructor-dashboard.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InstructorCoursesComponent } from './AllComponents/instructor-courses/instructor-courses.component';
import { InstructorProfileComponent } from './AllComponents/instructor-profile/instructor-profile.component';
import { InstructorAssignmentsComponent } from './AllComponents/instructor-assignments/instructor-assignments.component';
import { StudentCoursesComponent } from './AllComponents/student-courses/student-courses.component';
import { StudentProfileComponent } from './AllComponents/student-profile/student-profile.component';
import { StudentAssignmentsComponent } from './AllComponents/student-assignments/student-assignments.component';
import { StudentDashboardComponent } from './AllComponents/student-dashboard/student-dashboard.component';
import { CourseAddModalComponent } from './AllComponents/course-add-modal/course-add-modal.component';
import { CourseUpdateModalComponent } from './AllComponents/course-update-modal/course-update-modal.component';
import { SingleAssignmentComponent } from './AllComponents/single-assignment/single-assignment.component';
import { AddAssignmentModalComponent } from './AllComponents/add-assignment-modal/add-assignment-modal.component';
import { UpdateAssignmentModalComponent } from './AllComponents/update-assignment-modal/update-assignment-modal.component';



@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    NavbarComponent,
    HomeComponent,
    StudentLoginComponent,
    InstructorLoginComponent,
    InstructorDashboardComponent,
    InstructorCoursesComponent,
    InstructorProfileComponent,
    InstructorAssignmentsComponent,
    StudentCoursesComponent,
    StudentProfileComponent,
    StudentAssignmentsComponent,
    StudentDashboardComponent,
    CourseAddModalComponent,
    CourseUpdateModalComponent,
    SingleAssignmentComponent,
    AddAssignmentModalComponent,
    UpdateAssignmentModalComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
