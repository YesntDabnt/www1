class Calculator{
    constructor(previousOpTextElement, currentOpTextElement){
        this.previousOpTextElement = previousOpTextElement
        this.currentOpTextElement = currentOpTextElement
        this.clear()
    }

    clear(){
        this.currentOp = ''
        this.previousOp = ''
        this.operation = undefined
    }

    delete(){

    }

    appendNumber(number){
        if(number === '.' && this.currentOp.includes('.')) return
        this.currentOp = this.currentOp.toString() + number.toString()
    }

    chooseOperation(operation){
        if(this.currentOp === '') return
        if(this.previousOp !== ''){
            this.compute()
        }
        this.operation = operation
        this.previousOp = this.currentOp
        this.currentOp = ''
    }

    compute(){
        let computation
        const prev = parseFloat(this.previousOp)
        const current = parseFloat(this.currentOp)
        if (isNaN(prev) || isNaN(current)) return
        switch (this.operation) {
            case '+' : 
            computation = prev + current
            break
            case '-' : 
            computation = prev - current
            break
            case '*' : 
            computation = prev * current
            break
            case '/' : 
            computation = prev / current
            break
            default :
                return
        }
        this.currentOp = computation
        this.operation = undefined
        this.previousOp = ''
        
    }

    undateDisplay(){
        this.currentOpTextElement.innerText = this.currentOp
    }
}


const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButton = document.querySelector('[data-equals]')
const deleteButton = document.querySelector('[data-delete]')
const allClearButton = document.querySelector('[data-all-clear]')
const previousOpTextElement = document.querySelector('[data-previousOp]')
const currentOpTextElement = document.querySelector('[data-currentOp]')

const Calculator = new Calculator(previousOpTextElement,currentOpTextElement)

numberButtons.forEach(button => {
    button.addEventListener('click',() => {
    Calculator.appendNumber(button.innerText)
    Calculator.undateDisplay()
})
})

operationButtons.forEach(button => {
    button.addEventListener('click',() => {
    Calculator.appendNumber(button.innerText)
    Calculator.undateDisplay()
})
})

equalsButton.forEach(button => {
    button.addEventListener('click',() => {
        Calculator.compute()
        Calculator.undateDisplay()
})
})



