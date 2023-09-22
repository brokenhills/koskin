import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root'
})
export class HelperService {

    getShortContent(content: string): { content: string, length: number } {
        const split = content.split(' ');
        const contentLength = split.length;
        if (contentLength < 200) {
          return { content: content,  length: contentLength };
        }
        content = split.slice(0, 201).join(' ') + '...';
        return { content: content, length: contentLength };
      }
}
