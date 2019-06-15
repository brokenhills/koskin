export class NewsItem {

    idns: number;
    name: string;
    content: string;
    datead: string;

    constructor(values: Object = {}){
        Object.assign(this, values);
    }
}
