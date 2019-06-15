export class GalleryItem {
    
    idim: number;
    name: string;
    img: string;
    width_field: number;
    height_field: number;
    comment: string;
    datead: string;

    constructor(values: Object = {}) {
        Object.assign(this, values);
    }
}
