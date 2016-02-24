//
//  TableViewController.swift
//  MathNews
//
//  Created by cs laptop on 2/16/16.
//  Copyright (c) 2016 cs121MathNewApp. All rights reserved.
//

import UIKit

class TableViewController: UITableViewController {
    //MARK: Properties
    var articles = [String]()
    
    
    
    
    func loadSampleArticles(){
        let link1 = "Secret to the perfect pancake \ndescribed mathematically"
       // http://phys.org/news/2016-02-secret-pancake-mathematically.html"
        let link2 = "Corals, crochet and the cosmos:\n how hyperbolic geometry pervades the universe"
        //http://phys.org/news/2016-01-corals-crochet-cosmos-hyperbolic-geometry.html"
        let link3 = "The Intriguing Math That Turns\n Manhattan Properties Into Shekels"
        //http://www.bloomberg.com/news/articles/2016-02-15/the-intriguing-math-that-turns-manhattan-properties-into-shekels"
        
        articles+=[link1,link2,link3]
        
    }

    override func viewDidLoad() {
        super.viewDidLoad()

        //load the sample articles
        loadSampleArticles()

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
        cell.LinkLabel?.text = articles[indexPath.row]

        return cell
    }
    

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
