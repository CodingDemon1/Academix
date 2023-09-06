import { Component, Input, OnInit } from '@angular/core';
import { InstructorCoursesComponent } from '../instructor-courses/instructor-courses.component';
import { AuthService } from 'src/app/auth.service';
import { InstructorCourseService } from 'src/app/i-course.service';
import { Course } from '../instructor-courses/iCourseModel';

@Component({
  selector: 'app-course-update-modal',
  templateUrl: './course-update-modal.component.html',
  styleUrls: ['./course-update-modal.component.css']
})
export class CourseUpdateModalComponent  {

  @Input() currentCourse: any
  // @Input() sCourse: any
  // @Input() editedCourse: Course = new Course();

  // currentCourse : any = ''

  // ngOnInit(): void {
  //     const courseName = document.getElementById("courseName")
  //     const credits = document.getElementById("credits")
  //     const description = document.getElementById("description")
  //     const courseCode = document.getElementById("courseCode")



  // }

  user : any = ''
  modalVisible : boolean = false;
  constructor(private instComp : InstructorCoursesComponent, private authService: AuthService , private courseService: InstructorCourseService) {
  }

  closeModal(){
    this.instComp.closeUpdateModal()
  }

  updateCourse(){
    this.instComp.updateCourse(this.currentCourse, this.currentCourse.id)
  }
}
