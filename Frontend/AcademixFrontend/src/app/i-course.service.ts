import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { env } from 'src/environments/env';
import { Course } from './AllComponents/instructor-courses/iCourseModel';

@Injectable({
  providedIn: 'root'
})
export class InstructorCourseService {
  private apiUrl = env.apiURL; // Replace with your API URL

  constructor(private http: HttpClient) {}

  // Get a list of instructor courses
  getCourses(id:number): Observable<any> {
    return this.http.get<Course[]>(`${this.apiUrl}/courses/get-instructor-id/${id}/`);
  }

  // Add a new course
  addCourse(course: Course): Observable<any> {
    return this.http.post<Course>(`${this.apiUrl}/courses/add/`, course);
  }

  // Update a course
  updateCourse(course: Course, id:number): Observable<any> {
    console.log(course)
    return this.http.patch<Course>(`${this.apiUrl}/courses/update/${id}/`, course);
  }

  // Delete a course by its ID
  deleteCourse(courseId: number): Observable<any> {
    return this.http.delete<void>(`${this.apiUrl}/courses/delete/${courseId}/`);
  }
}
