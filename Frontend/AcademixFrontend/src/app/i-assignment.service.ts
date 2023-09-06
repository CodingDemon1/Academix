import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { iAssignment } from './AllComponents/instructor-assignments/iAssignment';
import { env } from 'src/environments/env';


@Injectable({
  providedIn: 'root'
})
export class AssignmentService {
  private apiUrl = env.apiURL; // Replace with your actual API URL

  constructor(private http: HttpClient) {}

  // Fetch assignments by course_id

  createAssignment(assignment:iAssignment): Observable<any> {
    const url = `${this.apiUrl}/assignments/add/`; // Adjust the endpoint accordingly
    return this.http.post<iAssignment>(url, assignment);
  }

  getAssignmentsByCourseId(courseId: number): any {
    const url = `${this.apiUrl}/assignments/get-by-course-id/${courseId}/`; // Adjust the endpoint accordingly
    return this.http.get<iAssignment[]>(url);
  }

  // Fetch a single assignment by assignmentId
  getAssignmentById(assignmentId: number): Observable<any> {
    const url = `${this.apiUrl}/assignments/${assignmentId}/`; // Adjust the endpoint accordingly
    return this.http.get<iAssignment>(url);
  }

  // Update an existing assignment
  updateAssignment(assignmentId: number, updatedAssignment: any): Observable<iAssignment> {
    const url = `${this.apiUrl}/assignments/update/${assignmentId}/`; // Adjust the endpoint accordingly
    return this.http.patch<iAssignment>(url, updatedAssignment);
  }

  // Delete an assignment by assignmentId
  deleteAssignment(assignmentId: number): any {
    const url = `${this.apiUrl}/assignments/delete/${assignmentId}/`; // Adjust the endpoint accordingly
    return this.http.delete<any>(url);
  }

}
