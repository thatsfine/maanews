//
//  TableViewController.swift
//  MathNews
//
//  Created by cs laptop on 2/16/16.
//  Copyright (c) 2016 cs121MathNewApp. All rights reserved.
//

import UIKit
import Firebase
//check to see if EMAIL works

class TableViewController: UITableViewController {
    //MARK: Properties
    var articles = [String]()
    var articleContent = [String]()

    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        var counter = 0
        //Create reference to database
        let ref = Firebase(url:"https://crackling-torch-4312.firebaseio.com")
        // Retrieve new posts as they are added to your database
        ref.observeEventType(.Value, withBlock: { snapshot in
           
            //
            for item in snapshot.children {
                let keysArray = Array((snapshot.value as! NSDictionary).allKeys as! [String])
                let title = snapshot.value[keysArray[counter]] as! String
                self.articles.append(title)
                self.articleContent.append("blurb will go here")
                ++counter
            }
            self.tableView.reloadData()
        })
       
       
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
      //  loadArticles()


    }

    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // Return the number of sections.
        return 1
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return articles.count
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentfier = "ArticleTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentfier, forIndexPath: indexPath) as!ArticleTableViewCell

        // Configure the cell...
        //title
        cell.LinkLabel?.text = articles[indexPath.row]
        
        //mini-content
        cell.ContentLabel?.text = articleContent[indexPath.row]
        
        

        return cell
    }
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        NSLog("You selected cell #\(indexPath.row)!")
       //opens the url to article depending on the cell that is clicked
        if(indexPath.row == 0){
            UIApplication.sharedApplication().openURL(NSURL(string: "http://phys.org/news/2016-02-secret-pancake-mathematically.html")!)}
        else if (indexPath.row==1){
            UIApplication.sharedApplication().openURL(NSURL(string: "http://phys.org/news/2016-01-corals-crochet-cosmos-hyperbolic-geometry.html")!)
        }
        else{
            UIApplication.sharedApplication().openURL(NSURL(string: "http://www.bloomberg.com/news/articles/2016-02-15/the-intriguing-math-that-turns-manhattan-properties-into-shekels")!)
        }
    }
    
    //


    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return NO if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using [segue destinationViewController].
        // Pass the selected object to the new view controller.
    }
    */
    
}
