export class MainInfo {

    idmn: string;
    name: string;
    content: string;
    datead: string;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
