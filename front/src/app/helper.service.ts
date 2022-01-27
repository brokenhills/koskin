import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root'
})
export class HelperService {

    getShortContent(content: string): { content: string, length: number } {
        const splitted = content.split(' ');
        const contentLength = splitted.length;
        if (contentLength < 200) {
          return { content: content,  length: contentLength };
        }
        content = splitted.slice(0, 201).join(' ') + '...';
        return { content: content, length: contentLength };
      }
}