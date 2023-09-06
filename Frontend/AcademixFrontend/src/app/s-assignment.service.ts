// assignment.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Assignment } from './AllComponents/student-assignments/assignment.model';
import { env } from 'src/environments/env';

@Injectable({
  providedIn: 'root',
})
export class SAssignmentService {
  private apiUrl = env.apiURL;
  constructor(private http: HttpClient) {}

  getAssignmentsByStudentId(studentId: number): Observable<Assignment[]> {
    // Example URL structure: /courses/assignments?courseIds=1,2,3
    return this.http.get<Assignment[]>(`${this.apiUrl}/enrollments/get-assignments-by-stId/${studentId}/`);
  }
}
