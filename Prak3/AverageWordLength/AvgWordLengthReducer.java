import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class AvgWordLengthReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int totalLength = 0;
        int wordCount = 0;

        for (IntWritable val : values) {
            totalLength += val.get();
            wordCount++;
        }

        int averageLength = totalLength / wordCount;
        context.write(new Text("Average Word Length: "), new IntWritable(averageLength));
    }
}
