// instructor-courses.component.ts

import { Component, Input, OnInit } from '@angular/core';
import { Course } from './iCourseModel';
import { InstructorCourseService } from 'src/app/i-course.service';
import { CourseAddModalComponent } from '../course-add-modal/course-add-modal.component';
import { AuthService } from 'src/app/auth.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-instructor-courses',
  templateUrl: './instructor-courses.component.html',
  styleUrls: ['./instructor-courses.component.css']
})
export class InstructorCoursesComponent implements OnInit {
  updateModalVisible : boolean = false;
  courses: any = [];
  modalVisible : boolean = false;
  userId !: number;
  constructor(private router: Router,private authServise: AuthService,private courseService: InstructorCourseService) {}

  ngOnInit(): void {
    this.userId = this.authServise.getUser().id
    this.loadCourses();
  }

  navigateToAssignments(courseId: number) {
  this.router.navigate(['instructor-dashboard/instructor/assignments', courseId]);
}


  loadCourses() {
    this.courseService.getCourses(this.userId).subscribe(res => {
      // this.courses = res.courses;
      console.log(res)
      this.courses = res.courses;
    },
    err => {
      console.log(err)
    }
    
    );
  }
  

  openModal() {
    this.modalVisible = true;
  }

  closeModal(){
    this.modalVisible = false;
  }
  openUpdateModal() {
    this.updateModalVisible = true;
  }

  closeUpdateModal(){
    this.updateModalVisible = false;
  }

  addCourse(newCourse: Course) {
    this.courseService.addCourse(newCourse).subscribe(

      res =>{
      if( res.response){
        alert(res.message)
      }
      this.closeModal()
      this.loadCourses();
      },
      err =>{
        console.log(err)
      }

    );
  }

  updateCourse(updatedCourse: Course, id: number) {
    this.courseService.updateCourse(updatedCourse, id).subscribe(
    res =>{
      if( res.response){
        alert(res.message)
      }
      this.closeUpdateModal()
      this.loadCourses();
      },
      err =>{
        console.log(err)
      }
      
    );
  }

  deleteCourse(courseId: number) {
    console.log(courseId)
    this.courseService.deleteCourse(courseId).subscribe(
      res =>{
        if(res.response){
          alert(res.message)
        }
        this.loadCourses();
      },
      err =>{
        console.log(err)
      }
    );
  }
}
