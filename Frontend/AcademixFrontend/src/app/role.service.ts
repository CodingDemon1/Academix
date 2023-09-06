import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RoleService {
  private userRoleSubject = new BehaviorSubject<string>(''); // Initialize with an empty string
  userRole$ = this.userRoleSubject.asObservable();

  setUserRole(role: string) {
    this.userRoleSubject.next(role);
  }
}
