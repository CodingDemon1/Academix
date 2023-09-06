import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from 'src/app/auth.service';
import { SCoursesService } from 'src/app/s-courses.service';
import { StudentService } from 'src/app/student.service';

@Component({
  selector: 'app-student-enrollments',
  templateUrl: './student-enrollments.component.html',
  styleUrls: ['./student-enrollments.component.css']
})
export class StudentEnrollmentsComponent implements OnInit {
  enrollments: any[] = []; // Replace 'any[]' with the actual type of your enrollments
  studentId!: number; // To store the student ID

  constructor(private authService : AuthService, private route: ActivatedRoute, private studentService: SCoursesService) {}

  ngOnInit(): void {
    this.studentId =  this.authService.getUser().id;

    this.fetchEnrollments()
  }

  fetchEnrollments(): void {
    this.studentService.getEnrollments(this.studentId).subscribe(
      (res: any) => {
        this.enrollments = res.enrollments
      }
    )
  }

  discontinueCourse(enrollmentId: number): void {
    // this.studentService.discontinueCourse(enrollmentId).subscribe(() => {
    //   this.fetchEnrollments();
    // });
  }
}
