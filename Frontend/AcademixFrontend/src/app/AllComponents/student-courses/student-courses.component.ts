import { Component, OnInit } from '@angular/core';
import { Course } from '../instructor-courses/iCourseModel';
import { SCoursesService } from 'src/app/s-courses.service';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-student-courses',
  templateUrl: './student-courses.component.html',
  styleUrls: ['./student-courses.component.css']
})
export class StudentCoursesComponent implements OnInit {
  userId : number = -1;
  courses : Course[] = []
  constructor(private sCourses : SCoursesService, private authService: AuthService){}
  ngOnInit(): void {
      
      this.userId = this.authService.getUser().id
      this.loadCourses()
  }

  loadCourses(){
    this.sCourses.getCourses().subscribe(
        res=>{
          this.courses = res.courses
        },
        err =>{
          console.log(err)
        }
      )
  }

  enrollCourse(courseId: number): void {
    const payload : object = {
        "student_id": this.userId,
        "course_id": courseId
    }
    this.sCourses.enrollCourse(payload).subscribe(
      (res : any)=>{
        alert(res.message)
      },
      (err: any) =>{
        console.log(err)
      }
    )
}
}

// id!: number;
//   course_code!: string;
//   course_name!: string;
//   credits!: number;
//   department!: string;
//   description!: string;
//   instructor_id!: number;