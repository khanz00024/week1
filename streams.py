def stream_flows():
    # Read the initial number of streams
    n = int(input())
    # Read the initial flow values
    streams = [float(input()) for _ in range(n)]

    while True:
        
        command = int(input())

        if command == 77: 
            break
        elif command == 99:  # Split
            stream_number = int(input()) - 1  # Convert to 0-based index
            percentage_left = int(input())
            flow = streams[stream_number]

            # Calculate flows for left and right forks
            left_flow = flow * (percentage_left / 100)
            right_flow = flow * (1 - (percentage_left / 100))

            
            streams[stream_number] = left_flow
            streams.insert(stream_number + 1, right_flow)

        elif command == 88:  # Join
            stream_number = int(input()) - 1  # Convert to 0-based index

            # Combine the specified stream with the stream to its right
            streams[stream_number] += streams[stream_number + 1]

            # Remove the right stream
            streams.pop(stream_number + 1)

    # Output the results
    print(" ".join(str(round(flow)) for flow in streams))



stream_flows()
