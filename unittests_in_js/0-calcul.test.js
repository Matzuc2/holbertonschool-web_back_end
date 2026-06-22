import assert from "node:assert";
import { calculateNumber

 } from "./0-calcul.js";
describe('calculateNumber', function(){
    it('round two number and add them up', function (){
        const result = calculateNumber(2.7,5)

        assert.strictEqual(result, 8)
    })
    it('should round the two arguments', function(){
        let a = 2.4
        let b = 1.8
        const result = calculateNumber(a,b)
        assert.strictEqual(result, 4)
    })
})