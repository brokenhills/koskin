export class Writing {

    idwr: number;
    name: string;
    genre: string;
    datewr: string;
    datead: string;
    content: string;
    description: string;
    is_liked: boolean;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
