import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.util.StringTokenizer;

public class AvgWordLengthMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable wordLength = new IntWritable(0);
    private final static Text wordKey = new Text("word_length");

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {
            String word = itr.nextToken();
            wordLength.set(word.length());
            context.write(wordKey, wordLength);
        }
    }
}
