public class FindMedianSortedArrays
{
	public static void Main()
	{
		int totalLen = nums1.Length + nums2.Length;
        float median;
        int middleIndex = (int) ((totalLen - 1) / 2);
        
        bool isEven = false;
        if(totalLen % 2 == 0)
            isEven = true;
        
        int i = 0;
        int j = 0; 
        int index = 0;
        int number = 0;
        int number2 = 0;
        while(index <= middleIndex)
        {
           
            if(i >= nums1.Length)
            {
                number = nums2[j];
                j += 1;
            }
            else if( j >= nums2.Length)
            {
                number = nums1[i];
                i += 1;
            }
            else if(nums1[i] < nums2[j])
            {
                number = nums1[i];
                i += 1;
            }
            else
            {
                number = nums2[j];
                j += 1 ;
            }
            index ++;
        }

        median = number;

        if(isEven)
        {
            if(i >= nums1.Length)
            {
                number2 = nums2[j];
                j += 1;
            }
            else if( j >= nums2.Length)
            {
                number2 = nums1[i];
                i += 1;
            }
            else if(nums1[i] < nums2[j])
            {
                number2 = nums1[i];
                i += 1;
            }
            else
            {
                number2 = nums2[j];
                j += 1 ;
            }
            median = (number + number2) / 2;
        }

        return median;
	}
}
