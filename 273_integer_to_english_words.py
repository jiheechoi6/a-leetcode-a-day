class Solution:
    to19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', "Fifty", 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    bigs = {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand'}
    def numberToWords(self, num: int) -> str:
        return ' '.join(self.words(num)) if num else 'Zero'

    def words(self, num: int):
        if num == 0:
            return []
        elif num < 20:
            return [self.to19[num-1]]
        elif num < 100:
            return [self.tens[num//10-2]] + self.words(num % 10)
        elif num < 1000:
            return [self.to19[num//100-1]] + ['Hundred'] + self.words(num % 100)
        else:
            for val, word in self.bigs.items():
                if num >= val:
                    return self.words(num//val) + [word] + self.words(num % val)
        
