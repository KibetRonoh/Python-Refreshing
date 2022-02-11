books = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in books:
    if status == "faulty":
        print("Stopping production Line")
        break # STOPPING THE LOOP, NO MORE ITERATIONS
    print(f"This car is {status}. ")
    print("Shipping New car to Customer")

#############################################
for status in books:
    if status == "faulty":
        print("Found Faulthy car, skipping production....")
        continue #SKIP THE FAULTY ONE AND GO TO THE NEXT ITARATION
    print(f"This car is {status}. ")
    print("Shipping New car to Customer")