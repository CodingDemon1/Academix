import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { Course } from '../instructor-courses/iCourseModel';
import { InstructorCourseService } from 'src/app/i-course.service';
import { InstructorCoursesComponent } from '../instructor-courses/instructor-courses.component';
import { AuthService } from 'src/app/auth.service';


@Component({
  selector: 'app-course-add-modal',
  templateUrl: './course-add-modal.component.html',
  styleUrls: ['./course-add-modal.component.css']
})
export class CourseAddModalComponent {
  @Input() visible: boolean = false;
  @Input() newCourse: Course = new Course(); // Input for the new course data
  @Output() addCourse: EventEmitter<Course> = new EventEmitter<Course>(); // Output event to add a course
  @Output() closeModalEvent = new EventEmitter<void>();
  
  user : any = ''
  modalVisible : boolean = false;
  constructor(private instComp : InstructorCoursesComponent, private authService: AuthService , private courseService: InstructorCourseService) {
  }

  closeModal() 
  {
    this.instComp.closeModal()
  }

  saveCourse() {
    this.user  = this.authService.getUser()
    this.newCourse.department = this.user.department;
    this.newCourse.instructor_id = this.user.id;
    this.instComp.addCourse(this.newCourse)
  }
}
