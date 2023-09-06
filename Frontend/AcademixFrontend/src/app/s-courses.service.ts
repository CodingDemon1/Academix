import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { env } from 'src/environments/env';
import { Course } from './AllComponents/instructor-courses/iCourseModel';

@Injectable({
  providedIn: 'root'
})
export class SCoursesService {
 private apiUrl = env.apiURL; // Replace with your API URL

  constructor(private http: HttpClient) {}

  // Get a list of instructor courses
  getCourses(): Observable<any> {
    return this.http.get<Course[]>(`${this.apiUrl}/courses/`);
  }

  enrollCourse(payload : any):any{  
      return this.http.post<object>(`${this.apiUrl}/enrollments/`,payload)
  }

  getEnrollments(studentId:number){
    return this.http.get<object>(`${this.apiUrl}/enrollments/student/${studentId}`)
  }

}
