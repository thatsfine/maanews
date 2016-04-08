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
    
    //create empty arrays for titles, blurbs, urls
    var titleArray = [String]()
    var blurbArray = [String]()
    var urlArray = [String]()

    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
        
        // Create reference to database
        // Currently references articles sub-category
        let ref = Firebase(url:"https://crackling-torch-4312.firebaseio.com/articles")
        
        // Retrieve new articles as they are added to your database
        ref.observeEventType(.ChildAdded, withBlock: { snapshot in
        
        //grab titles, blurbs, and urls from firebase
        let title = snapshot.value.objectForKey("title")!
        let blurb = snapshot.value.objectForKey("blurb")!
        let url = snapshot.value.objectForKey("url")!

        //add titles, blurbs, and urls to respective array
        //and convert to strings
        self.titleArray.append(title as! String)
        self.blurbArray.append(blurb as! String)
        self.urlArray.append(url as! String)
        
        //reload table with above data
        self.tableView.reloadData()
            
        }, withCancelBlock: { error in
                print(error.description)
        
        })
  
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
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
        return titleArray.count
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cellIdentfier = "ArticleTableViewCell"
        let cell = tableView.dequeueReusableCellWithIdentifier(cellIdentfier, forIndexPath: indexPath) as!ArticleTableViewCell

        //Configure the cell
        
        //Display title
        cell.LinkLabel?.text = titleArray[indexPath.row]
        
        //Display blurb
        cell.ContentLabel?.text = blurbArray[indexPath.row]
        

        return cell
    }
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        NSLog("You selected cell #\(indexPath.row)!")

        //opens URLs to news articles
        UIApplication.sharedApplication().openURL(NSURL(string: urlArray[indexPath.row])!)
    
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
