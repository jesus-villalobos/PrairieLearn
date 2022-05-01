class Middleware {
    constructor() {
        this.variantNum = 0;
        this.totalVariantNum = helperTemp();
    }

    nextVariant() {
        return ++this.variantNum % this.totalVariantNum;
    }

    prevVariant() {
        --this.variantNum;
        if (this.variantNum < 0) {
            this.variantNum = this.totalVariantNum - 1;
        }
        return this.variantNum;
    }

    selectVariant(num) {
        this.variantNum = num % this.totalVariantNum;
        return this.variantNum;
    }
}

function helperTemp() {
    var max = 100;
    var min = 1;
    return 10;
} 