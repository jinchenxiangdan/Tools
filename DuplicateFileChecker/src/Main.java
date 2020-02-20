import javax.xml.bind.DatatypeConverter;
import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

public class Main {
    private static HashMap<String, String> checksumHashMap = new HashMap<>();
    
    public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        // for testing 
        String testInputPath = "/home/wan/Desktop/ShawnJin_Workspace/Tools/DuplicateFileChecker/duplicate_test_folder";
        Path testPath = Paths.get(testInputPath);
        //
        System.out.println("Checking duplicate files...");
        File[] files = getFiles(testPath);

        Path currentPath;
        // loop directory 
        for (File file : files) {
            if (file.isDirectory()) {
                
            }
        }
        for (File file : files) {
            if (file.isFile())  System.out.println(file.getName() + ": " + getMD5CheckSum(file.toPath()));
        }
        System.out.println("--------------------");

    }

    /**
     * calculate the md5 checksum of a file
     * @param path the path to the file
     * @return a string of md5 encode
     * @throws NoSuchAlgorithmException
     * @throws IOException
     */
    private static String getMD5CheckSum(Path path) throws NoSuchAlgorithmException, IOException {
        MessageDigest messageDigest = MessageDigest.getInstance("MD5");
        messageDigest.update(Files.readAllBytes(path));
        return DatatypeConverter.printHexBinary(messageDigest.digest()).toUpperCase();
    }


    private static File[] getFiles(Path path) {
        File directory = new File(String.valueOf(path));
//        FilenameFilter isFile = (file, s) -> !file.isDirectory();
        return directory.listFiles();
    }
    
    private static void checkDuplicate(Path path) throws IOException, NoSuchAlgorithmException {
        File[] files = getFiles(path);
        boolean hasChecksum, hasFileName;
        for (File file : files) {
            String checksum = getMD5CheckSum(file.toPath());
            if (checksumHashMap.containsKey(checksum)) {
                hasChecksum = true;
            } else {
                hasChecksum = false;
            }
            
            if (checksumHashMap.containsValue(file.getName())) {
                hasFileName = true;
            } else {
                hasFileName = false;
            }
            
            
            
            if (!hasChecksum && !hasFileName) {
                // add to hashtable 
            } else if (!hasChecksum) {
                // move to folder <>
            } else if (!hasFileName) {
                // move to folder <>
            } else {
                // move to folder<>
            }
            
        }
    }
}
