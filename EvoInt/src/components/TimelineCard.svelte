<script lang="ts">
	export let position: string;
	export let date: string;
	export let heading: string;
	export let content: string;
</script>

{#if position === 'flex-col'}
	<div class="flex flex-col lg:flex-row justify-center items-center gap-12 lg:ml-[430px] black">
		<div
			class="flex justify-center items-center black bg-white z-50 rounded-[100%] w-32 h-32 font-mono text-xl"
		>
			{date}
		</div>
		<div
			class="block p-6 w-max max-w-sm rounded-lg border shadow-md bg-gray-800 border-gray-700 hover:bg-gray-700"
		>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-white">{heading}</h5>
			<p class="font-normal text-gray-300 text-base">{content}</p>
		</div>
	</div>
{:else}
	<div
		class="flex flex-col-reverse lg:flex-row justify-center items-center gap-12 lg:mr-[430px] black bg-red"
	>
		<div
			class="block p-6 w-max max-w-sm rounded-lg border shadow-md bg-gray-800 border-gray-700 hover:bg-gray-700"
		>
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-white">
				{heading}
			</h5>
			<p class="font-normal text-gray-300 text-base">
				{content}
			</p>
		</div>
		<div
			class="flex justify-center items-center black bg-white z-50 rounded-[100%] w-32 h-32 font-mono text-xl"
		>
			{date}
		</div>
	</div>
{/if}

<style lang="postcss">
</style>
