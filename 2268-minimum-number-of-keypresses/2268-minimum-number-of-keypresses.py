class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        char_frequency_dict = collections.Counter(s)
        
        # collections.Counter(str) will create a dict mapping letters to the count they appeared
        freq = sorted(char_frequency_dict.values(),reverse = True)
        
        # create a list for count of letters in decending order

		#Take a variable counter to check the position of Key press (First/Second/Third)
        counter,ans=0,0
        for ind,freq in enumerate(freq):
			# Counter will only increase when ind is divisble by 9 i.e 0,9,18
			#Ex:Counter=1 holds 0-8 key,value of char_frequency_dict Counter=2 holds 9 to 17 key:value of char_frequency_dict so on
            if ind%9==0:
                counter += 1
            ans += freq*counter
        return ans

        