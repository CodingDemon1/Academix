// modal.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ModalService {
  private showModalSubject = new BehaviorSubject<boolean>(false);
  showModal$ = this.showModalSubject.asObservable();

  constructor() {}

  openModal() {
    this.showModalSubject.next(true);
  }

  closeModal() {
    this.showModalSubject.next(false);
  }
}
