import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { WritingsComponent } from './writings.component';

describe('WritingsComponent', () => {
  let component: WritingsComponent;
  let fixture: ComponentFixture<WritingsComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ WritingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WritingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
